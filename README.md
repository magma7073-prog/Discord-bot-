# 🤖 Discord Bot

A simple Discord bot template to quickly create and run your own bot using **Node.js** and **discord.js**.

This project helps you easily set up a Discord bot, configure the token securely with a `.env` file, and start adding your own commands and features.

---

## 📦 Requirements

Before starting, make sure you have installed:

- **Node.js** (v18 or higher recommended)
- **npm** (comes with Node.js)

You can download Node.js here:  
https://nodejs.org

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/discord-bot.git
cd discord-bot
```

### 2. Install dependencies

Install the Discord library and other required packages:

```bash
npm install discord.js dotenv
```

---

## 🔑 Environment Variables

To keep your bot token secure, create a `.env` file in the root of the project.

```
TOKEN=your_discord_bot_token
```

Never share this token publicly.

---

## 🤖 Creating a Discord Bot

1. Go to the Discord Developer Portal  
https://discord.com/developers/applications

2. Click **New Application**

3. Give your bot a name

4. Go to the **Bot** section

5. Click **Add Bot**

6. Copy the **Bot Token**

7. Paste it into your `.env` file

---

## 📁 Project Structure

```
discord-bot/
│
├── index.js
├── .env
├── package.json
└── node_modules
```

---

## ▶️ Running the Bot

Start the bot with:

```bash
node index.js
```

If everything is configured correctly, your bot should appear **online on Discord**.

---

## 💡 Example Bot Code

Example `index.js`:

```js
require("dotenv").config();
const { Client, GatewayIntentBits } = require("discord.js");

const client = new Client({
  intents: [GatewayIntentBits.Guilds]
});

client.once("ready", () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.login(process.env.TOKEN);
```

---

## 🛠️ Technologies Used

- Node.js
- discord.js
- dotenv

---

## 📜 License

This project is open-source and free to use.
