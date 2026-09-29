from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)

MY_WHATSAPP = "2348106430205"

PRODUCTS = [
    {"name": "Supreme", "price": 13,700},
    {"name": "Superpack (120g)", "price": 15,000},
    {"name": "Superchicken", "price": 12,400},
    {"name": "Mimee", "price": 10,800},
    {"name": "Supreme (70g)", "price": 9,000},
    {"name": "Superpack (70g)", "price": 10,000},
    {"name": "Egg Crate", "price": 5,700},
]

# --- HOME PAGE ---
HOME_HTML = """
<!DOCTYPE html>
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Binmalik Shop - Indomie Yabo</title></head>
<body style="margin:0; font-family:sans-serif; background:#f2f4ff;">
<div style="background:#2F5BFF; color:white; padding:20px; text-align:center;">
  <h1 style="margin:0;">Binmalik Shop 🍜</h1>
  <p>Original Indomie Cartons - yabo Delivery</p>
</div>
<div style="max-width:500px; margin:auto; padding:15px;">
  {% for p in products %}
  <div style="background:white; padding:18px; border-radius:18px; margin-bottom:12px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 2px 8px rgba(0,0,0,0.08);">
    <div>
      <b style="font-size:17px;">{{ p.name }}</b><br>
      <span style="color:#FF6A00; font-weight:bold; font-size:18px;">₦{{ "{:,}".format(p.price) }}</span>
    </div>
    <a href="/order/{{ loop.index0 }}" style="background:#FF6A00; color:white; padding:10px 18px; border-radius:10px; text-decoration:none; font-weight:bold;">Order</a>
  </div>
  {% endfor %}
  <p style="text-align:center; color:gray; margin-top:20px;">📍 yabo, yabo | WhatsApp: 08106430205</p>
</div>
</body>
</html>
"""

# --- YOUR FAVOURITE INTERFACE FOR ORDER ---
ORDER_HTML = """
<div style="background:#2F5BFF; min-height:100vh; display:flex; align-items:center; justify-content:center; font-family:sans-serif; padding:15px;">
  <div style="background:white; padding:25px; border-radius:20px; animation: pop 0.6s ease; max-width:350px; width:100%; text-align:center;">
    <h2>🍜 Order Now</h2>
    <div style="background:#fff6f0; padding:15px; border-radius:12px; text-align:left; margin:15px 0;">
      <p style="margin:8px 0;"><b>Product:</b> {{ product.name }}</p>
      <p style="margin:8px 0;"><b>Price:</b> ₦{{ "{:,}".format(product.price) }}</p>
      <p style="margin:8px 0; color:green;"><b>Delivery:</b> Available in yabo</p>
    </div>
    <h3>Total: ₦{{ "{:,}".format(product.price) }}</h3>

    <a href="{{ wa_link }}" style="background:#25D366; color:white; padding:14px; width:100%; display:block; border:none; border-radius:12px; font-weight:bold; text-decoration:none; font-size:17px; box-sizing:border-box;">
      Confirm Order on WhatsApp ✓
    </a>
    <br>
    <a href="/" style="color:gray; text-decoration:none;">← Back to shop</a>
  </div>
</div>
<style>@keyframes pop{0%{transform:scale(0)}100%{transform:scale(1)}}</style>
"""

@app.route('/')
def home():
    return render_template_string(HOME_HTML, products=PRODUCTS)

@app.route('/order/<int:pid>')
def order_page(pid):
    product = PRODUCTS[pid]
    message = f"Hello Binmalik Shop, I want to order:\n\n* {product['name']} - ₦{product['price']:,}\n\nMy Name is:\nMy Address is:\nQuantity:"
    encoded_msg = urllib.parse.quote(message)
    wa_link = f"https://wa.me/{MY_WHATSAPP}?text={encoded_msg}"
    return render_template_string(ORDER_HTML, product=product, wa_link=wa_link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)