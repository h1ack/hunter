# 🏹 hunter  

Fast RECON for BugHunters  
Hunt: Run many tools in one for fast work

## 📦 Build

Clone the repository:

```bash
git clone https://github.com/h1ack/hunter.git
```

Navigate to the project folder:

```bash
cd hunter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

To run a quick scan on a target domain:

```bash
python3 hunt.py -d example.com
```

## ⚙️ Make it a Global Command

To move the script to a system-wide path so you can use `hunt` from anywhere:

```bash
sudo mv hunt.py /usr/local/bin/hunt
sudo chmod +x /usr/local/bin/hunt
```

Now you can simply use:

```bash
hunt -d example.com
```
