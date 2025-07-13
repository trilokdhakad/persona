import React, { useState } from 'react';
import './App.css';

const examplePersonas = [
  "A rebel street photographer from Tokyo",
  "A retired Soviet chess grandmaster in Iceland",
  "An anime-obsessed coder who loves street food",
  "A Berlin art critic who only watches arthouse cinema",
  "A jazz saxophonist living in 1980s New York"
];

function App() {
  const [personaInput, setPersonaInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleGenerate = async () => {
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/persona', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ persona: personaInput })
      });

      if (!response.ok) throw new Error('Server error');

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Failed to fetch response.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <h1>🧠 PersonaSwap</h1>
      <p>Enter a persona description:</p>

      <textarea
        rows="4"
        placeholder="e.g. A rebel street photographer from Tokyo"
        value={personaInput}
        onChange={(e) => setPersonaInput(e.target.value)}
      />

      <div className="persona-buttons">
        {examplePersonas.map((text, index) => (
          <button key={index} onClick={() => setPersonaInput(text)}>
            {text}
          </button>
        ))}
      </div>

      <button className="generate-button" onClick={handleGenerate} disabled={loading}>
        {loading ? 'Generating...' : 'Generate Taste Profile'}
      </button>

      {error && <p className="error-text">{error}</p>}

      {result && (
        <div className="result-block">
          <h2>🎨 Persona Profile</h2>
          <pre>{result.persona_profile}</pre>

          <h2>📡 Qloo Recommendations</h2>
          <pre>{JSON.stringify(result.qloo_data, null, 2)}</pre>

          <h2>📖 Narrative</h2>
          <p>{result.narrative}</p>
        </div>
      )}
    </div>
  );
}

export default App;
