import { useEffect, useState } from 'react'
import { supabase } from "@/lib/supabase"
import { Button } from '@/components/ui/button'
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

type Voice = {
    voice_id: string
    name: string
    description: string
}

export default function Settings() {
    const [voiceData, setVoiceData] = useState<Voice[]>([])

    useEffect(() => {
        const fetchVoices = async () => {
            const { data, error } = await supabase
                .from('voices')
                .select('voice_id, name, description')
            if (error) {
                console.error(error)
                return
            }
            setVoiceData((data ?? []) as Voice[])
        }
        fetchVoices()
    }, [])

    return (
        <>
            <Dialog>
                <DialogTrigger>
                    <Button variant="outline">Voices</Button>
                </DialogTrigger>
                <DialogContent>
                    <DialogHeader>
                        <DialogTitle>Voices</DialogTitle>
                        <DialogDescription>Choose a voice from the list below</DialogDescription>
                    </DialogHeader>
                    <RadioGroup>
                        {voiceData.map((voice) => (
                            <label key={voice.voice_id} className="flex items-center space-x-4 justify-between">
                                <RadioGroupItem value={voice.voice_id} id={voice.voice_id} />
                                <div className="flex flex-col w-full">
                                    <div className="text-left font-medium text-sm">{voice.name}</div>
                                    <div className="text-sm leading-tight text-gray-500 text-left">{voice.description}</div>
                                </div>
                                <Button size="sm" variant="outline">Preview voice</Button>
                            </label>
                        ))}
                    </RadioGroup>
                </DialogContent>
            </Dialog>
        </>
    )
}