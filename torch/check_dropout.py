for name, module in model.named_modules():
    if isinstance(module, torch.nn.Dropout):
        module.p = 0
