import argparse
import json
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import io


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--in', dest='infile', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--template', required=True)   # ADD THIS
    args = p.parse_args()

    signals = json.load(open(args.infile))

    # small chart placeholder
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.plot([1,2,3,2,3,4])
    ax.set_title('Mini Trend')
    buf = io.BytesIO()
    fig.savefig(buf, bbox_inches='tight')
    buf.seek(0)

    chart = Image.open(buf)

    # ---------------------------
    # LOAD YOUR PNG TEMPLATE HERE
    # ---------------------------
    card = Image.open(args.template).convert("RGBA")
    draw = ImageDraw.Draw(card)

    # paste chart at your desired coordinates
    chart = chart.resize((500, 250))  # adjust size
    card.paste(chart, (120, 180))     # adjust coordinates

    # Draw text
    draw.text((150, 480), f"Trend: {signals.get('trend')}", fill="white")
    draw.text((150, 520), f"Last:  {signals.get('last')}", fill="white")

    card.save(args.out)
    print('card ->', args.out)

'''
python render_card.py \
  --in signals.json \
  --out report.png \
  --template assets/bg.png
'''
