import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeJob = async () => {
    if (!text) {
      alert("Please enter job description");
      return;
    }

    try {
      setLoading(true);
      const res = await axios.post("https://ominous-space-giggle-g477rggjvprvcw6g6-5000.app.github.dev/predict", {
        text: text,
      });
      setResult(res.data);
    } catch (error) {
      console.error(error);
      alert("Cannot connect to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1 className="title">🔍 TrustHire</h1>
      <p className="subtitle">
        AI Powered Fake Job & Internship Detector
      </p>

      <div className="card">
        <textarea
          placeholder="Paste job description or internship posting here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button onClick={analyzeJob}>
          {loading ? "Analyzing..." : "Analyze Job"}
        </button>

        {result && (
          <div className="result-box">
            <h2>
              Result:{" "}
              <span
                className={
                  result.prediction === "Fake"
                    ? "fake-text"
                    : "legit-text"
                }
              >
                {result.prediction}
              </span>
            </h2>

            <p>Confidence: {(result.confidence * 100).toFixed(2)}%</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;