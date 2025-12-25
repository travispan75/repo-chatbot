"use client"

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");

  async function loadRepo(url: string) {
    const res = await fetch("/api/loadrepo", {
      method: "POST",
      body: JSON.stringify({ url }),
    });

    const data = await res.json();
    console.log(data);
  }

  return (
    <div className="flex items-center justify-center min-h-screen">
      <input
        placeholder="Enter GitHub URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button className="cursor-pointer" onClick={() => loadRepo(url)}>Analyze</button>
    </div>
  );
}
