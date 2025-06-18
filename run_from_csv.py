import pandas as pd
import traceback

def run_all_fits(new_LinearR, csv_file):
    df = pd.read_csv(csv_file)
    df.columns = df.columns.str.strip().str.lower()

    for index, row in df.iterrows():
        if pd.isna(row['sn']):
            continue

        sn_name = f"{row['sn']}.txt"  # Add .txt extension
        uvw2start = row['uvw2start']
        uvw2end = row['uvw2end']
        uvm2start = row['uvm2start']
        uvm2end = row['uvm2end']
        uvw1start = row['uvw1start']
        uvw1end = row['uvw1end']
        ustart = row['ustart']
        uend = row['uend']
        bstart = row['bstart']
        bend = row['bend']
        vstart = row['vstart']
        vend = row['vend']

        print(f"Running fit for {sn_name}...")
        try:
            print(f"Trying to open: {sn_name}")
            new_LinearR(
                sn_name,
                uvw2start, uvw2end,
                uvm2start, uvm2end,
                uvw1start, uvw1end,
                ustart, uend,
                vstart, vend,
                bstart, bend
            )
        except Exception as e:
            print(f"Failed on {sn_name}: {e}")
            traceback.print_exc()
