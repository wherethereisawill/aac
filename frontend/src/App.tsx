import './App.css'
import { Button } from '@/components/ui/button'
import Phrases from './components/Phrases'

function App() {

  return (
    <>
      <div className='flex flex-row justify-between mb-4'>
        <h1 className='text-3xl font-bold text-left'>AAC</h1>
        <Button variant="outline">Settings</Button>
      </div>
      <Phrases />
    </>
  )
}

export default App