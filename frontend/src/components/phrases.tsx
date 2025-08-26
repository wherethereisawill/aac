import { useState, useEffect } from 'react'
import { supabase } from "@/lib/supabase"
import { cn } from "@/lib/utils"
import { colourClassByName } from "@/utils/colours"
import AutoFitText from "@/components/AutoFitText"

type Phrase = {
  phrase_id: string
  text: string
  default_index: number
  default_colour: string
}

export default function Phrases() {

  const [phraseData, setPhraseData] = useState<Phrase[]>([])

  useEffect(() => {
    const fetchPhrases = async () => {
      const { data, error } = await supabase.from('phrases').select('phrase_id, text, default_index, default_colour')
      if (error) {
        console.error(error)
        return
      }
      setPhraseData((data ?? []) as Phrase[])
    }
    fetchPhrases()
  }, [])

  const handleClick = (phrase_id: string) => {
    const { data } = supabase.storage.from('audio').getPublicUrl(`${phrase_id}.mp3`)

    new Audio(data.publicUrl).play().catch(err => {
        console.error("Playback failed:", err)
      })
  }

  return (
    <div className='grid grid-cols-5 lg:grid-cols-10 gap-4'>
    {phraseData.map((item) => (
        <button 
            key={item.phrase_id}
            onClick={() => handleClick(item.phrase_id)} 
            className={cn(
              'flex flex-col p-1 border rounded-xl items-center justify-center border-4 cursor-pointer',
              colourClassByName[item.default_colour].bg,
              colourClassByName[item.default_colour].border
            )}
        >
        <AutoFitText text={item.text} />
        </button>
    ))}
    </div>
  )
}