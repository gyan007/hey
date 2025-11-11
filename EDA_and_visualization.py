import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_plot():
    
    # 1. Create a sample dataset (e.g., sales data)
    data = {
        'Product': ['Apple', 'Banana', 'Orange', 'Apple', 'Banana', 'Apple'],
        'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit'],
        'Quantity': [150, 200, 100, 180, 220, 130],
        'Price_per_Unit': [0.5, 0.3, 0.4, 0.55, 0.32, 0.48]
    }
    
    df = pd.DataFrame(data)
    
    print("--- Initial Data (First 5 rows) ---")
    print(df.head())
    print("\n")
    
    # 2. Perform Data Analysis
    
    # --- Basic Info ---
    print("--- Data Info ---")
    df.info()
    print("\n")
    
    # --- Descriptive Statistics ---
    print("--- Descriptive Statistics ---")
    print(df.describe())
    print("\n")
    
    # --- Feature Engineering: Create a new column ---
    df['Total_Sales'] = df['Quantity'] * df['Price_per_Unit']
    
    # --- Grouping and Aggregation ---
    print("--- Total Sales per Product ---")
    sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
    print(sales_by_product)
    print("\n")
    
    # 3. Generate Insightful Plots
    
    # --- Plot: Total Sales by Product ---
    plt.figure(figsize=(10, 6))
    
    # Create the bar plot
    sales_by_product.plot(kind='bar', color=['#4CAF50', '#FFC107', '#E91E63'])
    
    # Customize the plot
    plt.title('Total Sales by Product', fontsize=16, fontweight='bold')
    plt.xlabel('Product', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.xticks(rotation=0)  # Keep product names horizontal
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add data labels on top of the bars
    for index, value in enumerate(sales_by_product):
        plt.text(index, value + 5, f'${value:.2f}', ha='center', va='bottom')
        
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    
    # Save the plot to a file
    plot_filename = 'total_sales_by_product.png'
    plt.savefig(plot_filename)
    print(f"Plot saved successfully as '{plot_filename}'")
    
    # Display the plot
    plt.show()

# --- Main execution ---
if __name__ == "__main__":
    analyze_and_plot()