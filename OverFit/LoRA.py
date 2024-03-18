l1_penalty = sum(p.abs().sum() for p in model.parameters())


#Lora
l1_penalty = model.lora_A.abs().sum() + model.lora_B.abs().sum()

l2_penalty = sum(torch.sum(param ** 2) for param in model.parameters() if param.requires_grad)


# LLMs can easily get overfitted because of LoRA

# None of Weight Decay or L1 L2 worked
