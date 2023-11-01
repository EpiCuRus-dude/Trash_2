
def calculat(x_low, x_high, y_low, y_high):
    
    def joint_pdf(x, y):
        return 1

    
    joint_prob, _ = dblquad(joint_pdf, x_low, x_high, lambda x: y_low, lambda x: y_high)

    # Create meshgrid for plotting
    x_vals = np.linspace(0, 1, 100)
    y_vals = np.linspace(0, 1, 100)
    x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)

   
    joint_pdf_values = np.ones_like(x_mesh)

    
    plt.figure(figsize=(10, 10))
    plt.imshow(joint_pdf_values, extent=[0, 1, 0, 1], origin='lower', cmap='Blues', alpha=0.5)
    plt.colorbar(label='Joint PDF Value')

    # Highlight the area corresponding to the X and Y intervals
    plt.fill_betweenx([y_low, y_high], x_low, x_high, color='red', alpha=0.5)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Joint PDF of X and Y\nArea of Interest (P = {joint_prob:.2f})')

    plt.show()

    return joint_prob


calculate(0.2, 0.3, 0.4, 0.6)
