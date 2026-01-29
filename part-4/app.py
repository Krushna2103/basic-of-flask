from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# --------------------------------------------------
# HOME
# --------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------------------
# USER ROUTES
# --------------------------------------------------
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


# --------------------------------------------------
# POSTS
# --------------------------------------------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework.'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions.'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic.'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post=post, post_id=post_id)


# --------------------------------------------------
# EXERCISE 4.1 – PRODUCT PAGE
# --------------------------------------------------
@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 999.99},
        2: {'name': 'Phone', 'price': 699.99},
        3: {'name': 'Headphones', 'price': 199.99},
    }
    product = products.get(product_id)
    return render_template('product.html', product=product, product_id=product_id)


# --------------------------------------------------
# EXERCISE 4.2 – CATEGORY + PRODUCT
# --------------------------------------------------
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    products = {
        1: {'name': 'Laptop', 'price': 999.99},
        2: {'name': 'Phone', 'price': 699.99},
        3: {'name': 'Headphones', 'price': 199.99},
    }
    product = products.get(product_id)
    return render_template(
        'category_product.html',
        category=category_name,
        product=product,
        product_id=product_id
    )


# --------------------------------------------------
# EXERCISE 4.3 – SEARCH
# --------------------------------------------------
@app.route('/search')
def search_form():
    query = request.args.get('q')
    if query:
        return redirect(url_for('search_results', query=query))
    return render_template('search.html')


@app.route('/search/<query>')
def search_results(query):
    return render_template('search_results.html', query=query)


# --------------------------------------------------
# ABOUT + LINKS
# --------------------------------------------------
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/links')
def links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user': url_for('user_profile', username='Alice'),
        'post': url_for('show_post', post_id=1),
        'product': url_for('product_page', product_id=1),
    }
    return render_template('links.html', links=links)


# --------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
