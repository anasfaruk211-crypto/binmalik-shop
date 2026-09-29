from flask import Flask
app = Flask(__name__)

orders = []

@app.route('/')
def home():
    return """
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial; margin:0; background:#fff8f0}
.header{background:#ff6600; color:white; padding:25px; text-align:center}
.header h1{margin:0; font-size:32px}
.header p{margin:5px; font-size:18px}
.menu{padding:20px; max-width:600px; margin:auto}
.card{background:white; border-radius:15px; padding:20px; margin:15px 0; box-shadow:0 4px 10px rgba(0,0,0,0.1); border-left:6px solid #ff6600; display:flex; justify-content:space-between; align-items:center}
.card h3{margin:0; color:#333}
.price{color:#ff6600; font-weight:bold; font-size:20px}
.order-box{background:white; padding:20px; border-radius:15px; margin-top:20px; box-shadow:0 4px 10px rgba(0,0,0,0.1)}
input, select{width:100%; padding:12px; margin:8px 0; border-radius:8px; border:1px solid #ddd; font-size:16px}
button{background:#ff6600; color:white; border:none; padding:14px; width:100%; border-radius:10px; font-size:18px; font-weight:bold; cursor:pointer}
button:hover{background:#e65c00}
.footer{text-align:center; padding:15px; color:#888}
</style>
</head>
<body>
<div class="header">
<h1>🍜 Binmalik Indomie & Egg Center</h1>
<p>📍 Yabo LGA, Sokoto State - The Best Taste in Town!</p>
<p>📞 Call/WhatsApp: 08106430205 </p>
</div>

<div class="menu">
<h2>🔥 Our Menu</h2>

<div class="card">
<div><h3>🍳 Indomie + Egg</h3><small>Delicious + Fresh</small></div>
<div class="price">N15,000</div>
</div>

<div class="card">
<div><h3>🍳🍳 Indomie + 2 Eggs</h3><small>Double Egg Special</small></div>
<div class="price">N2,000</div>
</div>

<div class="card">
<div><h3>🔥 Indomie + Egg + Pepper</h3><small>Hot & Spicy</small></div>
<div class="price">N1,800</div>
</div>

<div class="card">
<div><h3>🥤 Extra Drink</h3><small>Coke, Fanta, Water</small></div>
<div class="price">N300</div>
</div>

<div class="order-box">
<h2>🛒 Place Your Order</h2>
<form action="/order" method="get">
<input name="name" placeholder="Your Name" required>
<input name="phone" placeholder="Your Phone Number" required>
<select name="food" required>
<option value="">Choose Food</option>
<option>Supreme Indomie - N13,700</option>
<option>Superpack - N15,000</option>
<option>Superchicken - N12,400</option>
<option>Mimee - N10,800</option>
<option>Egg - N5,700</option>
<option>Supreme 70g - N9000</option>
<option>superpack 70g - N10,000</option>
</select>
<button type="submit">Place Order Now 🚀</button>
</form>
</div>

</div>
<div class="footer">© 2026 Binmalik Shop - Made with ❤️ in Yabo</div>
</body>
</html>
    """

@app.route('/order')
def order():
    from flask import request
    name = request.args.get('name','Customer')
    food = request.args.get('food','')
    orders.append(f"{name} - {food}")
    return f"""
    <body style="font-family:Arial; text-align:center; padding:50px; background:#fff8f0">
    <h1 style="color:green">✅ Thank You {name}!</h1>
    <h2>Your order: {food}</h2>
    <p>We are preparing it now in Yabo!</p>
    <a href="/" style="background:#ff6600; color:white; padding:12px 20px; border-radius:10px; text-decoration:none">⬅️ Back to Menu</a>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)