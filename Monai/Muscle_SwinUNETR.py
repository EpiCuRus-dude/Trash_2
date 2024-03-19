# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ### If you have questions or issues you can send emails to Iman or John.

# +
# # +
import numpy as np
from monai.utils.enums import MetricReduction

from monai.utils import first, set_determinism
from monai.transforms import (
    Activations,
    RandFlipd,
    RandRotate90d,
    RandShiftIntensityd,
    AsDiscrete,
    AsDiscreted,
    EnsureChannelFirstd,
    Compose,
    CropForegroundd,
    LoadImaged,
    Orientationd,
    RandCropByPosNegLabeld,
    ScaleIntensityRanged,
    Spacingd,
    Invertd,
    SpatialPadd,
    NormalizeIntensity,
    NormalizeIntensityd,
    Resized,
    EnsureTyped
)


from monai.inferers import sliding_window_inference
from monai.data import decollate_batch

import os
import glob
import json
def save_pet(pet, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(pet))

def load_pet(filename):
    with open(filename) as f:
        pet = json.loads(f.read())
    return pet



# +

roi_x_model = 128
roi_y_model = 128
roi_z_model = 64

roi_x = 128
roi_y = 128
roi_z = 64

roi = (roi_x, roi_y, roi_z)
import torch
device = torch.device("cuda:1")
from monai.data import CacheDataset, DataLoader, Dataset, load_decathlon_datalist

num_samples = 1
train_transforms = Compose(
    [
        LoadImaged(keys=["image", "label"]),
        EnsureChannelFirstd(keys=["image", "label"]),
        ScaleIntensityRanged(
            keys=["image"],
            a_min=-500,
            a_max=500,
            b_min=0.0,
            b_max=1.0,
            clip=True,
        ),
        CropForegroundd(keys=["image", "label"], source_key="image"),
        Orientationd(keys=["image", "label"], axcodes="RAS"),
        Spacingd(keys=["image", "label"], pixdim=(1, 1, 3), mode=("bilinear", "nearest")),
        SpatialPadd(keys=['image', 'label'],
        spatial_size= (roi_x, roi_y, roi_z)),
         RandCropByPosNegLabeld(
            keys=["image", "label"],
            label_key="label",
            spatial_size=(roi_x, roi_y, roi_z),
            pos=1,
            neg=1,
            num_samples=1,
            image_key="image",
            image_threshold=0,
        ),
         RandFlipd(
            keys=["image", "label"],
            spatial_axis=[0],
            prob=0.10,
        ),
        RandFlipd(
            keys=["image", "label"],
            spatial_axis=[1],
            prob=0.10,
        ),
        RandFlipd(
            keys=["image", "label"],
            spatial_axis=[2],
            prob=0.10,
        ),
        RandRotate90d(
            keys=["image", "label"],
            prob=0.10,
            max_k=3,
        ),
        RandShiftIntensityd(
            keys=["image"],
            offsets=0.10,
            prob=0.50,
        ),
        # user can also add other random transforms
        # RandAffined(
        #     keys=['image', 'label'],
        #     mode=('bilinear', 'nearest'),
        #     prob=1.0, spatial_size=(96, 96, 96),
        #     rotate_range=(0, 0, np.pi/15),
        #     scale_range=(0.1, 0.1, 0.1)),
    ]
)
val_transforms = Compose(
    [
        LoadImaged(keys=["image", "label"], ensure_channel_first=True),
        ScaleIntensityRanged(keys=["image"], a_min=-500, a_max=500, b_min=0.0, b_max=1.0, clip=True),
        CropForegroundd(keys=["image", "label"], source_key="image"),
        Orientationd(keys=["image", "label"], axcodes="RAS"),
        Spacingd(
            keys=["image", "label"],
            pixdim=(1, 1, 3),
            mode=("bilinear", "nearest"),
        ),
        EnsureTyped(keys=["image", "label"], track_meta=True),
    ]
)

# -



# +

data_list_file_path = ...
loaded_dic = load_pet(data_list_file_path)

train_files = loaded_dic["Train_data_dicts"]

print(train_files)


val_files =  loaded_dic["val_data_dicts"]



# +
batch_size_train = 10

train_ds = Dataset(data=train_files, transform=train_transforms)
train_loader = DataLoader(train_ds, batch_size=batch_size_train)
#train_data = first(train_loader)

print(len(train_loader))

# -



# +
batch_size_val =1

val_ds = Dataset(data=val_files, transform=val_transforms)
val_loader = DataLoader(val_ds, batch_size=batch_size_val)
# -


print(len(val_loader))





# +
path_train = "./Train_samp"
if not os.path.exists(path_train):
        os.mkdir(path_train)

path_val = "./val_samp"
if not os.path.exists(path_val):
        os.mkdir(path_val)

root_dir = "./Res"
if not os.path.exists(root_dir):
        os.mkdir(root_dir)

loss_dir = "./loss"
if not os.path.exists(loss_dir):
        os.mkdir(loss_dir) 

# +
####################
#### model
import monai

#### model
import monai

from monai.networks.nets import SwinUNETR
from monai.networks.nets import UNet
## Create Model, Loss, Optimizer
max_epochs = 30000000
val_interval = 1
VAL_AMP = True




import monai


model = SwinUNETR(
    img_size=(roi_x_model, roi_y_model, roi_z_model),
    in_channels=1,
    out_channels=1,
    feature_size=48,
    use_checkpoint=True,
).to(device)

# -

path = "./best_metric_model.pth"

model.load_state_dict(torch.load(path, map_location=str(device)))

print("--->", path, " is loaded.")
model.to(device)



# +
from monai.losses import DiceCELoss
from monai.metrics import DiceMetric

loss_function = DiceCELoss(include_background=True)
dice_metric = DiceMetric(include_background=True, reduction="mean")

act_sigmoid = torch.nn.Sigmoid()


optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=1e-5)
lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

# -



# define inference method
def inference(input, roi):

    def _compute(input, roi):
        return sliding_window_inference(
            inputs=input,
            roi_size=roi,
            sw_batch_size=1,
            predictor=model,
            overlap=0.25,
        )

    if VAL_AMP:
        with torch.cuda.amp.autocast():
            return _compute(input, roi)
    else:
        return _compute(input, roi)



# +
# # +
import time
# use amp to accelerate training
scaler = torch.cuda.amp.GradScaler()
# enable cuDNN benchmark
torch.backends.cudnn.benchmark = True


best_metric = 0
best_metric_epoch = 0
epoch_loss_values = []
metric_values0 = []


# -



# +


post_label = Compose([Activations(sigmoid=True)])
post_pred = Compose([Activations(sigmoid=True), AsDiscrete(threshold=0.5)])


# -



# +

import nibabel as nib

x_file = nib.load('/src/workspace/John/Muscle_Seg/Muscle_Seg/DataSet/data/0.nii')   
y_file = nib.load('/src/workspace/John/Muscle_Seg/Muscle_Seg/DataSet/label/0.nii')  

# -



# +

total_start = time.time()
for epoch in range(max_epochs):
    epoch_start = time.time()
    print("-" * 10)
    print(f"epoch {epoch + 1}/{max_epochs}")
    
    
    model.train()
    
    
    
    epoch_loss = 0
    step = 0
    
    idx = 0
    ### First time
    
    
    
    for batch_data in train_loader:
        print(f" ===> Train: Epoch[{epoch+1}/{max_epochs}]->[{idx+1}]/[{len(train_loader)}]")
        
        step_start = time.time()
        step += 1
        #print(batch_data["image"])
        #print(batch_data["label"])
        inputs, labels = (
            batch_data["image"].to(device),
            batch_data["label"].to(device),
        )
        
        print(f'inputs.shape={inputs.shape}')
        print(f'labels.shape={labels.shape}')
        
        #for param in model.parameters():
        #    param.grad = None
        
        
        optimizer.zero_grad()
        with torch.cuda.amp.autocast():
            outputs0 = model(inputs)
            
            outputs = act_sigmoid(outputs0)
            
            loss_1 = loss_function(outputs, labels)
            
            print(f'outputs.shape={outputs.shape}')

            
            #loss_2 = loss_SSIM(labels.squeeze(0), outputs.squeeze(0), labels.max().unsqueeze(0))
            
            #print(f'\n\n\n \t = {loss_2}' )
                        
            loss = (loss_1) #+ loss_2
            
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
        epoch_loss += loss.item()
        print(
            f"{step}/{len(train_ds) // train_loader.batch_size}"
            f", train_loss: {loss.item():.4f}"
            f", step time: {(time.time() - step_start):.4f}"
        )
        
        
        if idx%5==0:
                import nibabel as nib
                
                        ##############################################################
                #print(np.shape(outputs))
                predW = outputs.cpu().detach().numpy()[0,0,:,:,:]
                #print(f'np.shape(predW)={np.shape(predW)}')
                pred_img = nib.Nifti1Image(predW, y_file.affine, y_file.header)
                path_img = path_train + '/'+str(idx) +'_Pred_sig.nii'
                #print(f'path_img={path_img}')
                nib.save(pred_img, path_img) 
                
                #print(np.shape(outputs))
                predW = outputs0.cpu().detach().numpy()[0,0,:,:,:]
                #print(f'np.shape(predW)={np.shape(predW)}')
                pred_img = nib.Nifti1Image(predW, y_file.affine, y_file.header)
                path_img = path_train + '/'+str(idx) +'_Pred.nii'
                #print(f'path_img={path_img}')
                nib.save(pred_img, path_img) 
                
                
                

                x = inputs.cpu().detach().numpy()[0,0,:,:,:]
                x_img = nib.Nifti1Image(x, x_file.affine, x_file.header)
                path_img_x = path_train + '/'+str(idx) +'_X.nii'
                #print(f'path_img={path_img_x}')
                nib.save(x_img, path_img_x) 

                y = labels.cpu().detach().numpy()[0,0,:,:,:]
                #print(f'np.shape(y)={np.shape(y)}')
                y_img = nib.Nifti1Image(y, y_file.affine, y_file.header)
                path_img_y = path_train + '/'+str(idx) +'_Y.nii' 
                #print(f'path_img={path_img_y}')
                nib.save(y_img, path_img_y) 
                ############################################################


        idx +=1
        
        
        
    lr_scheduler.step()
    epoch_loss = np.mean(epoch_loss)
    epoch_loss_values.append(epoch_loss)
    print(f"epoch {epoch + 1} average loss: {epoch_loss:.4f}")
    np.save("./loss/epoch_loss_"+"train"+"_{:03d}.npy".format(epoch+1), epoch_loss_values)
    
    
    
    
    id_val = 0
    epoch_val_loss0 = 0
    if (epoch + 1) % val_interval == 0:
        model.eval()
        with torch.no_grad():

            for val_data in val_loader:
                #print(np.shape(outputs))
                #print(np.shape(val_labels))
                print(f" ===> Val: Epoch[{epoch+1}/{max_epochs}]->[{id_val+1}]/[{len(val_loader)}]")
                
                
                val_inputs, val_labels = (
                    val_data["image"].to(device),
                    val_data["label"].to(device),
                )
                
                print(f'val_inputs.shape={val_inputs.shape}')
                print(f'val_labels.shape={val_labels.shape}')
                
                roi = (128,128,128)
                
                val_outputs = inference(val_inputs, roi)
                
                
                
                val_labels_convert = val_labels#post_label(val_labels)
                
                
                
                val_output_convert = post_pred(val_outputs)
                
                """
                print(f'val_outputs.shape={val_outputs.shape}')
                
                val_labels_list = decollate_batch(val_labels)
                
                print(f'val_labels_list.shape={val_labels_list[0].shape},{len(val_labels_list)}')
                
                val_labels_convert = [post_label(val_label_tensor) for val_label_tensor in val_labels_list]
                
                print(f'val_labels_convert.shape={val_labels_convert[0].shape},{len(val_labels_convert)}')
                
                val_outputs_list = decollate_batch(val_outputs)
                
                print(f'val_outputs_list.shape={val_outputs_list[0].shape},{len(val_outputs_list)}')
                
                val_output_convert = [post_pred(val_pred_tensor) for val_pred_tensor in val_outputs_list]
                
                print(f'val_output_convert.shape={val_output_convert[0].shape},{len(val_output_convert)}')
                
                print(f'\n\n\n before saving')
                """
                
                
                if id_val == 0:
                     ##############################################################
                    #print(np.shape(outputs))
                    
                    
                    
                    predW = val_outputs.cpu().detach().numpy()[0,0,:,:,:]
                    #print(f'np.shape(predW)={np.shape(predW)}')
                    pred_img = nib.Nifti1Image(predW, y_file.affine, y_file.header)
                    path_img = path_val + '/'+str(id_val) +'_Pred.nii'
                    #print(f'path_img={path_img}')
                    nib.save(pred_img, path_img) 
                    
                   

                    x = val_inputs.cpu().detach().numpy()[0,0,:,:,:]
                    x_img = nib.Nifti1Image(x, x_file.affine, x_file.header)
                    path_img_x = path_val + '/'+str(id_val) +'_X.nii'
                    #print(f'path_img={path_img_x}')
                    nib.save(x_img, path_img_x) 

                    y = val_labels.cpu().detach().numpy()[0,0,:,:,:]
                    #print(f'np.shape(y)={np.shape(y)}')
                    y_img = nib.Nifti1Image(y, y_file.affine, y_file.header)
                    path_img_y = path_val + '/'+str(id_val) +'_Y.nii' 
                    #print(f'path_img={path_img_y}')
                    nib.save(y_img, path_img_y) 
                    
                    
                    y = val_labels_convert.cpu().detach().numpy()[0,0,:,:,:]
                    #print(f'np.shape(y)={np.shape(y)}')
                    y_img = nib.Nifti1Image(y, y_file.affine, y_file.header)
                    path_img_y = path_val + '/'+str(id_val) +'_Y_convert.nii' 
                    #print(f'path_img={path_img_y}')
                    nib.save(y_img, path_img_y)
                    
                    
                    predW = val_output_convert.cpu().detach().numpy()[0,0,:,:,:]
                    #print(f'np.shape(predW)={np.shape(predW)}')
                    pred_img = nib.Nifti1Image(predW, y_file.affine, y_file.header)
                    path_img = path_val + '/'+str(id_val) +'_Pred_convert.nii'
                    #print(f'path_img={path_img}')
                    nib.save(pred_img, path_img)
                    
                    
                    
                    
                    
                    
                    
                    ############################################################
                    
                id_val += 1
                
                print(f'\n\n\n before dice metric')
                dice_metric(y_pred=val_output_convert, y=val_labels_convert)
  
                
               
                
                


            mean_dice_val = dice_metric.aggregate().item()
            
            print(f'\n\n\nmean_dice_val={mean_dice_val}\n\n\n\n')
            
            dice_metric.reset()
            
            acc = mean_dice_val
                
          
            
            metric_values0.append(acc)
            #metric_values2.append(metric2)
            #metric_values1.append(metric1)
            
            np.save("./loss/epoch_loss_"+"val"+"_{:03d}.npy".format(epoch+1), metric_values0)
            #np.save("./loss/epoch_loss_"+"val1"+"_{:03d}.npy".format(epoch+1), metric_values1)
            #np.save("./loss/epoch_loss_"+"val2"+"_{:03d}.npy".format(epoch+1), metric_values2)
            metric = acc
            

            
            if metric > best_metric:
                best_metric = metric
                best_metric_epoch = epoch + 1
                #best_metrics_epochs_and_time[0].append(best_metric)
                #best_metrics_epochs_and_time[1].append(best_metric_epoch)
                #best_metrics_epochs_and_time[2].append(time.time() - total_start)
                torch.save(
                    model.state_dict(),
                    os.path.join(root_dir, "best_metric_model.pth"),
                )
                print("saved new best metric model")
            print(
                f"current epoch: {epoch + 1} current loss: {metric:.4f}"
                #f" tc: {metric_tc:.4f} wt: {metric_wt:.4f} et: {metric_et:.4f}"
                #f"\nbest mean dice: {best_metric:.4f}"
                #f" at epoch: {best_metric_epoch}"
            )


# -




















