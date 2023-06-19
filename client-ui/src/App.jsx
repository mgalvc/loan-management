import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [fields, setFields] = useState([])
  const [proposal, setProposal] = useState({})

  useEffect(() => {
	// Fetches the proposal fields created on Django admin
	fetch('http://127.0.0.1:8000/api/proposal-fields')
		.then(res => res.json())
		.then(setFields)
  }, [])

  const sendProposal = (e) => {
	const request = {
		method: 'POST',
		body: JSON.stringify({metadata: proposal}),
		headers: { 'Content-Type': 'application/json' }
	}
	fetch('http://127.0.0.1:8000/api/proposals', request)
  }

  return (
    <>
	  <h2>Proposta de Empréstimo</h2>
	  <form onSubmit={sendProposal}>
		{
			// Renders form inputs with the fields fetched from the API
			fields.map(f => (
				<div key={f.field_name}>
					<label>{f.field_name}</label><br />
					<input 
						id={f.field_name} 
						onChange={(e) => setProposal(p => ({...p, [f.field_name]: e.target.value}))} 
						required
					/>
				</div>
			))
		}
		<div>
			<button type='submit'>Enviar</button>
		</div>
	</form>
    </>
  )
}

export default App
