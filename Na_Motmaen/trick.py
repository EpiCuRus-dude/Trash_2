with torch.no_grad():
        for _ in range(n_samples):
            model.train()  # Enable dropout during inference
            predictions.append(model(input_data).numpy())
