import os
import pandas as pd
import matplotlib.pyplot as plt

# Наш проверенный точный путь к чистому файлу
file_path = r"C:\Users\User\Desktop\fashion_analysis\fashion_boutique_dataset_CLEAN.csv"

if not os.path.exists(file_path):
    print("ERROR: Clean data file not found!")
else:
    df = pd.read_csv(file_path)
    folder_path = os.path.dirname(file_path)

    print("Generating charts...")

    # ——— ГРАФИК 1: ВЫРУЧКА БРЕНДОВ ———
    brand_revenue = df.groupby('brand')['current_price'].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    # Рисуем симпатичные столбцы цвета морской волны
    brand_revenue.plot(kind='bar', color='#4682B4', edgecolor='black')
    
    plt.title('Total Revenue by Brand ($)', fontsize=14, fontweight='bold')
    plt.xlabel('Brand', fontsize=12)
    plt.ylabel('Revenue', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Добавим легкую сетку
    plt.tight_layout()

    # Сохраняем первый график в папку проекта
    chart1_path = os.path.join(folder_path, "revenue_by_brand.png")
    plt.savefig(chart1_path, dpi=300) # dpi=300 — это высокое качество картинки
    plt.close()
    print(f"1. Saved: {chart1_path}")


    # ——— ГРАФИК 2: ПРИЧИНЫ ВОЗВРАТОВ ———
    return_counts = df[df['return_reason'] != 'No Return']['return_reason'].value_counts()

    plt.figure(figsize=(10, 6))
    # Рисуем горизонтальные столбцы мягкого кораллового цвета
    return_counts.plot(kind='barh', color='#E06666', edgecolor='black')
    
    plt.title('Top Reasons for Product Returns', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Returns', fontsize=12)
    plt.ylabel('Reason', fontsize=12)
    plt.gca().invert_yaxis() # Самая частая причина будет вверху
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Сохраняем второй график в папку проекта
    chart2_path = os.path.join(folder_path, "return_reasons.png")
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"2. Saved: {chart2_path}")

    print("\n Success! All charts generated. Check your project folder!")