import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";

type VoiceState = {
  voice_id: string;
  setVoiceId: (id: string) => void;
  clear: () => void;
};

export const useVoiceStore = create<VoiceState>()(
  persist(
    (set) => ({
      voice_id: "d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d",
      setVoiceId: (id) => set({ voice_id: id }),
      clear: () => set({ voice_id: "d9ed509b-e830-4ca2-b7f2-21bbb5c9e54d" }),
    }),
    {
      name: "voice-store", // key in localStorage
      storage: createJSONStorage(() => localStorage),
      partialize: (s) => ({ voice_id: s.voice_id }), // only persist voice_id
      version: 1,
    }
  )
);