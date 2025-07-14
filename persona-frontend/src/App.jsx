import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [personaInput, setPersonaInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [saved, setSaved] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchSavedPersonas();
  }, []);

  const fetchSavedPersonas = async () => {
    const res = await fetch('http://localhost:8000/personas');
    const data = await res.json();
    setSaved(data);
  };

  const handleGenerate = async () => {
    setLoading(true);
    setResult(null);
    setError(null);

    try {
      const response = await fetch('http://localhost:8000/persona', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ persona: personaInput })
      });

      if (!response.ok) throw new Error('Server error');

      const data = await response.json();
      setResult(data);
      fetchSavedPersonas();
    } catch (err) {
      setError('Failed to fetch response.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>PersonaSwap</h1>
      <p>Enter a persona description:</p>

      <textarea
        className="textarea"
        rows="4"
        placeholder="e.g. A rebel street photographer from Tokyo"
        value={personaInput}
        onChange={(e) => setPersonaInput(e.target.value)}
      />
      <br />
      <button onClick={handleGenerate} disabled={loading} className="button">
        {loading ? 'Generating...' : 'Generate Taste Profile'}
      </button>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <div className="card">
            <h2>🎨 Persona Profile</h2>
            <p><strong>{result.persona}</strong></p>
            <p>{result.summary}</p>
          </div>

          <div className="card">
            <h2>📡 Qloo Recommendations</h2>
            <ul>
              {Object.entries(result.qloo_data).map(([k, v]) => (
                <li key={k}><strong>{k}</strong>: {v.join(', ')}</li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {saved.length > 0 && (
        <div className="saved">
          <h2>🗂 Saved Personas</h2>
          {saved.map((item, idx) => (
            <div className="card" key={idx}>
              <strong>{item.persona}</strong><br />
              <small>{item.summary.slice(0, 80)}...</small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
