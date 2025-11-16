# 🍵 Brewtopia Coffeehouse - Full-Stack Web Application

A beautiful, feature-rich coffee shop management system built with Flask, PostgreSQL, and modern web technologies.

## ✨ Features

- 🔐 **User Authentication** - Registration, login, secure sessions
- 🛒 **E-Commerce** - Shopping cart, online ordering, order tracking
- 📅 **Reservations** - Table booking system with availability checking
- 🎁 **Loyalty Program** - Points system for repeat customers
- 🎨 **Beautiful UI** - Animated, responsive design with coffee themes
- 📱 **Mobile-First** - Fully responsive across all devices
- ☁️ **Cloud Ready** - PostgreSQL database for production deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL
- Git

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd brewtopia
pip install -r requirements.txt
```

### 2. PostgreSQL Setup

#### Option A: Automated Setup (Recommended)

```bash
# Make sure PostgreSQL is installed and running
python setup_postgres.py
```

#### Option B: Manual Setup

1. **Install PostgreSQL:**
   - **Windows:** Download from [postgresql.org](https://www.postgresql.org/download/windows/)
   - **macOS:** `brew install postgresql`
   - **Ubuntu:** `sudo apt-get install postgresql postgresql-contrib`

2. **Create Database and User:**
   ```sql
   -- Connect to PostgreSQL as superuser
   psql -U postgres

   -- Create database and user
   CREATE DATABASE brewtopia_db;
   CREATE USER brewtopia_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE brewtopia_db TO brewtopia_user;
   \q
   ```

3. **Configure Environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

### 3. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:3000/` in your browser!

## 🗄️ Database Configuration

### Local Development

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://brewtopia_user:your_password@localhost:5432/brewtopia_db
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
```

### Production Deployment

#### Heroku

1. **Create Heroku App:**
   ```bash
   heroku create your-app-name
   ```

2. **Add PostgreSQL Add-on:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

The `DATABASE_URL` will be automatically set by Heroku.

#### AWS/DigitalOcean

1. **Set Environment Variables:**
   ```bash
   export DATABASE_URL="postgresql://user:password@host:5432/database"
   export SECRET_KEY="your-production-secret-key"
   ```

2. **Use a WSGI Server:**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

## 📁 Project Structure

```
brewtopia/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── setup_postgres.py     # Database setup script
├── .env.example          # Environment variables template
├── .env                  # Environment variables (create from example)
├── templates/            # Jinja2 templates
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── cart.html
│   ├── checkout.html
│   ├── order_history.html
│   ├── reservations.html
│   └── make_reservation.html
├── static/               # Static assets
│   ├── style.css
│   ├── script.js
│   └── images/
└── README.md
```

## 🔧 API Endpoints

### Authentication
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `POST /logout` - User logout

### E-Commerce
- `GET /` - Home page with menu
- `GET /cart` - Shopping cart
- `POST /add_to_cart/<item_id>` - Add item to cart
- `POST /remove_from_cart/<item_id>` - Remove item from cart
- `GET/POST /checkout` - Checkout process
- `GET /order_history` - Order history

### Reservations
- `GET /reservations` - User's reservations
- `GET/POST /make_reservation` - Make new reservation

## 🛠️ Development

### Running Tests

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```

### Code Formatting

```bash
# Install black and flake8
pip install black flake8

# Format code
black .

# Check style
flake8 .
```

## 🚀 Deployment Options

### Docker Deployment

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .
   CMD ["python", "app.py"]
   ```

2. **Build and Run:**
   ```bash
   docker build -t brewtopia .
   docker run -p 3000:3000 brewtopia
   ```

### Cloud Platforms

- **Heroku:** `git push heroku main`
- **AWS Elastic Beanstalk:** Use EB CLI
- **Google Cloud Run:** Containerized deployment
- **DigitalOcean App Platform:** Direct Git integration

## 🔒 Security Features

- CSRF protection with Flask-WTF
- Password hashing with Werkzeug
- Secure session management
- SQL injection prevention with SQLAlchemy
- Environment variable configuration

## 📱 Progressive Web App (PWA) Ready

The application includes PWA features:
- Responsive design
- Fast loading
- Offline capabilities (can be extended)
- Mobile-friendly interface

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Database Connection Issues

1. **Check PostgreSQL is running:**
   ```bash
   # Linux
   sudo systemctl status postgresql

   # macOS
   brew services list | grep postgresql
   ```

2. **Test database connection:**
   ```bash
   python -c "from app import db, app; app.app_context().push(); print('Connection successful!')"
   ```

3. **Reset database:**
   ```bash
   python -c "from app import db, app; app.app_context().push(); db.drop_all(); db.create_all(); print('Database reset!')"
   ```

### Common Errors

- **"Peer authentication failed"**: Use password authentication or run as postgres user
- **"Database does not exist"**: Create the database first
- **"Connection refused"**: Check PostgreSQL is running on correct port

## 📞 Support

For support, please create an issue in the GitHub repository or contact the development team.

---

Made with ☕ and ❤️ for coffee lovers everywhere!