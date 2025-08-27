import './App.css'
import { Button } from '@/components/ui/button'
import Settings from '@/components/Settings'
import Phrases from '@/components/Phrases'

function App() {

  return (
    <>
      <div className='flex flex-row justify-between mb-4'>
        <h1 className='text-3xl font-bold text-left'>AAC</h1>
        <div className='flex flex-row gap-2'>
          <Button disabled>Add phrase</Button>
          <Settings />
        </div>
      </div>
      <Phrases />
    </>
  )
}

export default App