import os
import pandas as pd

# Жестко указываем точный путь к твоему чистому файлу на Рабочем столе
file_path = (r"C:\Users\User\Desktop\fashion_analysis\fashion_boutique_dataset_CLEAN.csv")

print("============ FASHION BUSINESS INSIGHTS ============\n")

if not os.path.exists(file_path):
    print("ERROR: Clean data file not found at the expected path.")
    print(f"Expected path: {file_path}")
    
    # Посмотрим, как на самом деле называется файл в папке
    folder_path = os.path.dirname(file_path)
    if os.path.exists(folder_path):
        print(f"Actual files in folder: {os.listdir(folder_path)}")
else:
    # Если файл на месте, запускаем анализ
    df = pd.read_csv(file_path)

    # 1. Markdown Loss
    df['markdown_loss'] = df['original_price'] - df['current_price']
    total_loss = df['markdown_loss'].sum()
    print(f"Total revenue lost to discounts: ${total_loss:,.2f}\n")

    # 2. Return Reasons
    print("Top reasons for product returns:")
    return_counts = df[df['return_reason'] != 'No Return']['return_reason'].value_counts()
    print(return_counts)
    print("\n")

    # 3. Brand Revenue
    print("Total revenue by brand:")
    brand_revenue = df.groupby('brand')['current_price'].sum().sort_values(ascending=False)

    for brand, rev in brand_revenue.items():
        print(f"   {brand}: ${rev:,.2f}")

    print("\n==================================================")