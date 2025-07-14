import os
import json
import requests
import shutil

# === CONFIGURATION ===
TIERS_FILE = "tiers.json"
OUTPUT_ROOT = "output"
ALL_DOWNLOADS_DIR = os.path.join(OUTPUT_ROOT, "all_downloads")
KEYS_TO_DOWNLOAD = [
    "LC Ubers",
    "LC OU",
    "LC UU BL",
    "LC UU",
    "LC RU BL",
    "LC RU",
    "The rest"
] 

# === HELPERS ===
def read_json_file(path):
    with open(path, "r") as f:
        return json.load(f)

def get_existing_pokemon(folder):
    return {f.replace(".png", "") for f in os.listdir(folder) if f.endswith(".png")}

def download_sprite(pokemon_name, folder_path):
    filename = f"{pokemon_name}.png"
    file_path = os.path.join(folder_path, filename)

    if os.path.exists(file_path):
        # print(f"🟡 Skipped (already exists): {pokemon_name} in {os.path.basename(folder_path)}")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['sprites']['front_default']
        if image_url:
            img_data = requests.get(image_url).content
            with open(file_path, 'wb') as f:
                f.write(img_data)
            print(f"✅ Downloaded: {pokemon_name} → {folder_path}")
        else:
            print(f"⚠️ No image for {pokemon_name}")
    else:
        print(f"❌ Error fetching {pokemon_name}: {response.status_code}")

def create_aggregate_folders(base_dir, tiers, exclusion_steps):
    for excluded_tiers in exclusion_steps:
        included_tiers = [t for t in tiers if t not in excluded_tiers]

        folder_name = "all_but_" + "_and_".join(t.lower().replace(" ", "_") for t in excluded_tiers)
        folder_path = os.path.join(base_dir, folder_name)

        # Remove old aggregate folder
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"🗑️ Deleted old aggregate folder: {folder_name}")

        os.makedirs(folder_path, exist_ok=True)
        print(f"\n📦 Rebuilding aggregate: {folder_name} (includes: {included_tiers})")

        added = set()
        for tier in included_tiers:
            tier_folder = os.path.join(base_dir, tier)
            if not os.path.exists(tier_folder):
                continue

            for fname in sorted(os.listdir(tier_folder)):
                if not fname.endswith(".png") or fname in added:
                    continue
                src_path = os.path.join(tier_folder, fname)
                dst_path = os.path.join(folder_path, fname)
                shutil.copy2(src_path, dst_path)
                added.add(fname)
                # print(f"➕ {fname}")


# === MAIN ===
def main():
    # Step 1: Load tiers
    if not os.path.exists(TIERS_FILE):
        print(f"❌ Missing file: {TIERS_FILE}")
        return

    tiers = read_json_file(TIERS_FILE)

    # Step 2: Create all_downloads folder
    os.makedirs(ALL_DOWNLOADS_DIR, exist_ok=True)
    downloaded_all = get_existing_pokemon(ALL_DOWNLOADS_DIR)

    # Step 3: Process each tier
    for tier, pokemon_list in tiers.items():
        if tier not in KEYS_TO_DOWNLOAD:
            continue

        tier_folder = os.path.join(OUTPUT_ROOT, tier)
        os.makedirs(tier_folder, exist_ok=True)

        target_set = set(map(str.lower, pokemon_list))
        existing_set = get_existing_pokemon(tier_folder)

        # Remove outdated Pokémon
        for poke in existing_set - target_set:
            file_path = os.path.join(tier_folder, f"{poke}.png")
            os.remove(file_path)
            print(f"🗑️ Removed: {poke} from {tier}")

        # Download missing Pokémon
        for poke in sorted(target_set):
            download_sprite(poke, tier_folder)
            if poke not in downloaded_all:
                download_sprite(poke, ALL_DOWNLOADS_DIR)
                downloaded_all.add(poke)

    # Step 4: Create aggregate folders every time
    exclusion_steps = [
        ["LC Ubers"],
        ["LC Ubers", "LC OU", "LC UU BL"],
        ["LC Ubers", "LC OU", "LC UU BL", "LC UU"]
    ]
    create_aggregate_folders(OUTPUT_ROOT, tiers, exclusion_steps)

if __name__ == "__main__":
    main()
