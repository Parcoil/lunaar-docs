# Running Locally

You can run Lunaar locally or on a server by following these steps:

## Prerequisites

- Node.js 22
- PNPM
- (Optional) Groq API key for Luna AI

## Step 1: Clone the Repository

```sh
git clone https://github.com/Parcoil/lunaar.org
cd lunaar.org
```

## Step 1.5: Install PNPM (if not already installed)

If you already have PNPM installed, skip to Step 2.

```sh
npm install -g pnpm@latest
```

## Step 2: Install Dependencies

```sh
pnpm install
```

## Step 3: Start Lunaar

```sh
pnpm start
```

## Setting up Luna AI

### 1. Get a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key (it starts with `gsk_`)

### 2. Configure Environment Variables

Create a `.env` file in your project root with:

```bash
GROQ_API_KEY=your_actual_groq_api_key_here
```

## Updating Lunaar

To keep Lunaar up to date (highly recommended to run once a week):

```sh
cd lunaar.org
git pull
```
