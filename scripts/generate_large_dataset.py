"""
Synthetic Laptop Dataset Generator
Generates 400,000+ realistic laptop entries based on market patterns
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define realistic laptop specifications based on market data
BRANDS = {
    'Apple': {'weight': 0.12, 'price_multiplier': (2.0, 3.5)},
    'Dell': {'weight': 0.18, 'price_multiplier': (0.9, 1.8)},
    'HP': {'weight': 0.16, 'price_multiplier': (0.8, 1.6)},
    'Lenovo': {'weight': 0.15, 'price_multiplier': (0.85, 1.7)},
    'Asus': {'weight': 0.13, 'price_multiplier': (0.9, 1.9)},
    'Acer': {'weight': 0.10, 'price_multiplier': (0.75, 1.5)},
    'MSI': {'weight': 0.06, 'price_multiplier': (1.5, 2.8)},
    'Razer': {'weight': 0.03, 'price_multiplier': (2.2, 3.2)},
    'Microsoft': {'weight': 0.04, 'price_multiplier': (1.8, 2.5)},
    'Samsung': {'weight': 0.03, 'price_multiplier': (0.9, 1.7)}
}

TYPES = {
    'Notebook': 0.35,
    'Ultrabook': 0.20,
    'Gaming': 0.15,
    'Workstation': 0.12,
    '2 in 1 Convertible': 0.10,
    'Netbook': 0.05,
    '2-in-1': 0.03
}

SCREEN_SIZES = {
    11.6: 0.05,
    13.3: 0.25,
    14.0: 0.20,
    15.6: 0.35,
    17.3: 0.10,
    12.0: 0.03,
    15.4: 0.02
}

RESOLUTIONS = {
    '1366x768': {'quality': 'HD', 'price_factor': 0.8},
    '1920x1080': {'quality': 'Full HD', 'price_factor': 1.0},
    '2560x1440': {'quality': 'QHD', 'price_factor': 1.3},
    '2560x1600': {'quality': 'Retina', 'price_factor': 1.5},
    '2880x1800': {'quality': 'Retina', 'price_factor': 1.6},
    '3840x2160': {'quality': '4K', 'price_factor': 1.8},
    '1600x900': {'quality': 'HD+', 'price_factor': 0.9},
    '2304x1440': {'quality': 'Retina', 'price_factor': 1.4}
}

CPUS = {
    # Intel Processors
    'Intel Core i3 6006U 2GHz': {'base_score': 25, 'price': 15000, 'generation': 6},
    'Intel Core i3 7100U 2.4GHz': {'base_score': 28, 'price': 16000, 'generation': 7},
    'Intel Core i3 8130U 2.2GHz': {'base_score': 32, 'price': 18000, 'generation': 8},
    'Intel Core i5 7200U 2.5GHz': {'base_score': 45, 'price': 25000, 'generation': 7},
    'Intel Core i5 8250U 1.6GHz': {'base_score': 55, 'price': 30000, 'generation': 8},
    'Intel Core i5 8300H 2.3GHz': {'base_score': 60, 'price': 35000, 'generation': 8},
    'Intel Core i5 10210U 1.6GHz': {'base_score': 58, 'price': 32000, 'generation': 10},
    'Intel Core i5 11300H 3.1GHz': {'base_score': 65, 'price': 38000, 'generation': 11},
    'Intel Core i7 7500U 2.7GHz': {'base_score': 55, 'price': 35000, 'generation': 7},
    'Intel Core i7 8550U 1.8GHz': {'base_score': 65, 'price': 40000, 'generation': 8},
    'Intel Core i7 8750H 2.2GHz': {'base_score': 80, 'price': 50000, 'generation': 8},
    'Intel Core i7 10750H 2.6GHz': {'base_score': 85, 'price': 55000, 'generation': 10},
    'Intel Core i7 11800H 2.3GHz': {'base_score': 95, 'price': 65000, 'generation': 11},
    'Intel Core i9 9980HK 2.4GHz': {'base_score': 100, 'price': 75000, 'generation': 9},
    'Intel Core i9 11900H 2.5GHz': {'base_score': 110, 'price': 85000, 'generation': 11},

    # AMD Processors
    'AMD Ryzen 3 3200U 2.6GHz': {'base_score': 30, 'price': 18000, 'generation': 3},
    'AMD Ryzen 5 3500U 2.1GHz': {'base_score': 48, 'price': 28000, 'generation': 3},
    'AMD Ryzen 5 4600H 3.0GHz': {'base_score': 70, 'price': 38000, 'generation': 4},
    'AMD Ryzen 5 5600H 3.3GHz': {'base_score': 75, 'price': 42000, 'generation': 5},
    'AMD Ryzen 7 4800H 2.9GHz': {'base_score': 85, 'price': 48000, 'generation': 4},
    'AMD Ryzen 7 5800H 3.2GHz': {'base_score': 95, 'price': 55000, 'generation': 5},
    'AMD Ryzen 9 5900HX 3.3GHz': {'base_score': 105, 'price': 70000, 'generation': 5},

    # Entry level
    'Intel Celeron N4020 1.1GHz': {'base_score': 15, 'price': 10000, 'generation': 10},
    'Intel Pentium N5030 1.1GHz': {'base_score': 20, 'price': 12000, 'generation': 10},
    'AMD A9-Series 9420 3GHz': {'base_score': 22, 'price': 13000, 'generation': 9},
}

RAM_OPTIONS = [2, 4, 8, 12, 16, 24, 32, 64]  # GB
RAM_PRICES = {2: 2000, 4: 4000, 8: 8000, 12: 12000, 16: 16000, 24: 24000, 32: 32000, 64: 64000}

STORAGE_CONFIG = {
    '128GB SSD': {'price': 3000, 'score': 20},
    '256GB SSD': {'price': 5000, 'score': 30},
    '512GB SSD': {'price': 8000, 'score': 45},
    '1TB SSD': {'price': 15000, 'score': 60},
    '2TB SSD': {'price': 28000, 'score': 75},
    '500GB HDD': {'price': 2000, 'score': 15},
    '1TB HDD': {'price': 3000, 'score': 20},
    '2TB HDD': {'price': 5000, 'score': 25},
    '256GB SSD + 1TB HDD': {'price': 8000, 'score': 50},
    '512GB SSD + 1TB HDD': {'price': 11000, 'score': 65},
    '1TB SSD + 2TB HDD': {'price': 20000, 'score': 85},
}

GPUS = {
    # Integrated
    'Intel HD Graphics 620': {'price': 0, 'gaming_score': 10},
    'Intel UHD Graphics 620': {'price': 0, 'gaming_score': 12},
    'Intel Iris Plus Graphics 640': {'price': 0, 'gaming_score': 15},
    'Intel Iris Xe Graphics': {'price': 0, 'gaming_score': 25},
    'AMD Radeon Graphics': {'price': 0, 'gaming_score': 20},

    # Entry Dedicated
    'Nvidia GeForce MX150': {'price': 8000, 'gaming_score': 30},
    'Nvidia GeForce MX250': {'price': 10000, 'gaming_score': 35},
    'Nvidia GeForce MX350': {'price': 12000, 'gaming_score': 40},
    'Nvidia GeForce MX450': {'price': 15000, 'gaming_score': 45},
    'AMD Radeon RX 5500M': {'price': 18000, 'gaming_score': 50},

    # Mid-range Gaming
    'Nvidia GeForce GTX 1650': {'price': 25000, 'gaming_score': 60},
    'Nvidia GeForce GTX 1660Ti': {'price': 35000, 'gaming_score': 70},
    'Nvidia GeForce RTX 3050': {'price': 40000, 'gaming_score': 75},
    'Nvidia GeForce RTX 3050Ti': {'price': 45000, 'gaming_score': 80},
    'AMD Radeon RX 6600M': {'price': 42000, 'gaming_score': 78},

    # High-end Gaming
    'Nvidia GeForce RTX 3060': {'price': 55000, 'gaming_score': 85},
    'Nvidia GeForce RTX 3070': {'price': 75000, 'gaming_score': 92},
    'Nvidia GeForce RTX 3080': {'price': 95000, 'gaming_score': 98},
    'AMD Radeon RX 6800M': {'price': 80000, 'gaming_score': 94},
}

OS_OPTIONS = {
    'Windows 10': 0.35,
    'Windows 11': 0.30,
    'macOS': 0.12,
    'No OS': 0.15,
    'Linux': 0.05,
    'Chrome OS': 0.03
}

def generate_laptop_entry():
    """Generate a single realistic laptop entry"""

    # Select brand with weighted probability
    brand = random.choices(list(BRANDS.keys()),
                          weights=[v['weight'] for v in BRANDS.values()])[0]
    brand_info = BRANDS[brand]

    # Select type
    laptop_type = random.choices(list(TYPES.keys()),
                                 weights=list(TYPES.values()))[0]

    # Screen size
    screen_size = random.choices(list(SCREEN_SIZES.keys()),
                                 weights=list(SCREEN_SIZES.values()))[0]

    # Resolution (higher-end brands get better screens)
    if brand in ['Apple', 'Razer', 'Microsoft']:
        resolution_choices = ['2560x1600', '2880x1800', '3840x2160', '2304x1440']
    elif laptop_type == 'Gaming':
        resolution_choices = ['1920x1080', '2560x1440', '3840x2160']
    elif laptop_type == 'Netbook':
        resolution_choices = ['1366x768', '1600x900']
    else:
        resolution_choices = list(RESOLUTIONS.keys())

    resolution = random.choice(resolution_choices)
    res_info = RESOLUTIONS[resolution]

    # Screen quality prefix
    screen_prefix = ''
    if res_info['quality'] in ['Retina', '4K']:
        screen_prefix = 'IPS Panel Retina Display ' if brand == 'Apple' else 'IPS Panel Full HD '
    elif random.random() > 0.7:
        screen_prefix = 'Full HD ' if resolution == '1920x1080' else ''

    screen_resolution = f"{screen_prefix}{resolution}".strip()

    # CPU selection based on type
    if laptop_type == 'Gaming' or laptop_type == 'Workstation':
        cpu_options = [k for k, v in CPUS.items() if v['base_score'] >= 60]
    elif laptop_type == 'Netbook':
        cpu_options = [k for k, v in CPUS.items() if v['base_score'] <= 25]
    elif brand == 'Apple':
        cpu_options = [k for k in CPUS.keys() if 'Intel Core i5' in k or 'Intel Core i7' in k or 'Intel Core i9' in k]
    else:
        cpu_options = list(CPUS.keys())

    cpu = random.choice(cpu_options)
    cpu_info = CPUS[cpu]

    # RAM based on type and brand
    if laptop_type in ['Gaming', 'Workstation']:
        ram = random.choices([16, 32, 64], weights=[0.5, 0.4, 0.1])[0]
    elif laptop_type == 'Netbook':
        ram = random.choices([2, 4], weights=[0.4, 0.6])[0]
    elif brand == 'Apple':
        ram = random.choices([8, 16, 32], weights=[0.4, 0.4, 0.2])[0]
    else:
        ram = random.choices(RAM_OPTIONS, weights=[0.05, 0.15, 0.35, 0.15, 0.20, 0.05, 0.04, 0.01])[0]

    # Storage based on type
    if laptop_type in ['Gaming', 'Workstation']:
        storage_options = ['512GB SSD', '1TB SSD', '2TB SSD', '512GB SSD + 1TB HDD', '1TB SSD + 2TB HDD']
    elif laptop_type == 'Netbook':
        storage_options = ['128GB SSD', '256GB SSD', '500GB HDD']
    elif brand == 'Apple':
        storage_options = ['256GB SSD', '512GB SSD', '1TB SSD', '2TB SSD']
    else:
        storage_options = list(STORAGE_CONFIG.keys())

    storage = random.choice(storage_options)
    storage_info = STORAGE_CONFIG[storage]

    # GPU based on type
    if laptop_type == 'Gaming':
        gpu_options = [k for k, v in GPUS.items() if v['gaming_score'] >= 60]
    elif laptop_type == 'Workstation':
        gpu_options = [k for k, v in GPUS.items() if v['gaming_score'] >= 40]
    elif brand == 'Apple':
        gpu_options = ['Intel Iris Plus Graphics 640', 'Intel Iris Xe Graphics', 'AMD Radeon Graphics']
    else:
        # Weighted selection - more integrated GPUs for regular laptops
        integrated = [k for k, v in GPUS.items() if v['gaming_score'] <= 25]
        dedicated = [k for k, v in GPUS.items() if v['gaming_score'] > 25]
        gpu_options = random.choices([integrated, dedicated], weights=[0.7, 0.3])[0]

    gpu = random.choice(gpu_options)
    gpu_info = GPUS[gpu]

    # OS
    if brand == 'Apple':
        os = 'macOS'
    elif laptop_type == 'Netbook':
        os = random.choices(['Windows 10', 'Windows 11', 'Chrome OS'], weights=[0.3, 0.3, 0.4])[0]
    else:
        os = random.choices(list(OS_OPTIONS.keys()), weights=list(OS_OPTIONS.values()))[0]

    # Weight based on screen size and type
    base_weight = screen_size / 10
    if laptop_type == 'Gaming':
        base_weight += random.uniform(0.3, 0.8)
    elif laptop_type == 'Ultrabook':
        base_weight -= random.uniform(0.2, 0.5)

    weight = round(max(0.8, base_weight + random.uniform(-0.2, 0.3)), 2)

    # Calculate price
    base_price = cpu_info['price']
    base_price += RAM_PRICES[ram]
    base_price += storage_info['price']
    base_price += gpu_info['price']
    base_price += res_info['price_factor'] * 5000

    # Brand multiplier
    price_mult = random.uniform(*brand_info['price_multiplier'])
    base_price *= price_mult

    # Type adjustments
    if laptop_type == 'Gaming':
        base_price *= random.uniform(1.2, 1.5)
    elif laptop_type == 'Workstation':
        base_price *= random.uniform(1.3, 1.6)
    elif laptop_type == 'Ultrabook':
        base_price *= random.uniform(1.1, 1.3)
    elif laptop_type == 'Netbook':
        base_price *= random.uniform(0.6, 0.8)

    # Add random variance
    base_price *= random.uniform(0.92, 1.08)

    # Convert to INR and round
    price = round(base_price, 2)

    return {
        'Company': brand,
        'TypeName': laptop_type,
        'Inches': screen_size,
        'ScreenResolution': screen_resolution,
        'Cpu': cpu,
        'Ram': f'{ram}GB',
        'Memory': storage,
        'Gpu': gpu,
        'OpSys': os,
        'Weight': f'{weight}kg',
        'Price': price
    }

def generate_dataset(num_entries=400000):
    """Generate the full dataset"""
    print(f"🚀 Generating {num_entries:,} laptop entries...")
    print("This will take a few minutes...\n")

    laptops = []
    batch_size = 10000

    for i in range(0, num_entries, batch_size):
        batch_end = min(i + batch_size, num_entries)
        print(f"⚙️  Generating entries {i:,} to {batch_end:,}...")

        for j in range(batch_size):
            if i + j >= num_entries:
                break
            laptops.append(generate_laptop_entry())

        # Show progress
        progress = (batch_end / num_entries) * 100
        print(f"   Progress: {progress:.1f}% complete")

    print("\n✅ Generation complete! Creating DataFrame...")
    df = pd.DataFrame(laptops)

    # Add index
    df.reset_index(drop=True, inplace=True)

    return df

def validate_dataset(df):
    """Validate the generated dataset"""
    print("\n📊 Dataset Statistics:")
    print(f"   Total entries: {len(df):,}")
    print(f"   Columns: {list(df.columns)}")
    print(f"\n💰 Price Range: ₹{df['Price'].min():,.0f} - ₹{df['Price'].max():,.0f}")
    print(f"   Average Price: ₹{df['Price'].mean():,.0f}")
    print(f"\n🏢 Brand Distribution:")
    print(df['Company'].value_counts().head(5))
    print(f"\n💻 Type Distribution:")
    print(df['TypeName'].value_counts())
    print(f"\n🔧 Sample Entries:")
    print(df.head(3).to_string())

    # Check for nulls
    nulls = df.isnull().sum().sum()
    print(f"\n✓ Null values: {nulls} (should be 0)")

    return True

if __name__ == "__main__":
    print("=" * 70)
    print("   LAPTOP DATASET GENERATOR - 400K+ ENTRIES")
    print("=" * 70)
    print()

    # Generate the dataset
    df = generate_dataset(num_entries=400000)

    # Validate
    validate_dataset(df)

    # Save to CSV
    output_file = 'laptop_data_400k.csv'
    print(f"\n💾 Saving to {output_file}...")
    df.to_csv(output_file, index=True)

    print(f"\n✅ SUCCESS! Dataset saved to {output_file}")
    print(f"   File size: {len(df):,} rows")
    print(f"   Columns: {len(df.columns)}")
    print("\n🎯 You can now use this dataset with your ML model!")
    print("=" * 70)
