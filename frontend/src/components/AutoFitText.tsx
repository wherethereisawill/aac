import { useEffect, useRef, useState } from 'react'
import { cn } from '@/lib/utils'

type AutoFitTextProps = {
  text: string
  className?: string
  minFontPx?: number
  maxFontPx?: number
}

export default function AutoFitText({
  text,
  className,
  minFontPx = 10,
  maxFontPx = 24,
}: AutoFitTextProps) {
  const containerRef = useRef<HTMLDivElement | null>(null)
  const [computedFontSize, setComputedFontSize] = useState<number>(maxFontPx)

  useEffect(() => {
    const container = containerRef.current
    if (!container) return

    const measureAndFit = () => {
      if (!container) return

      // Guard against zero-width containers
      const availableWidth = container.clientWidth
      if (availableWidth === 0) {
        return
      }

      // Binary search for largest font size that fits
      let low = minFontPx
      let high = maxFontPx
      let best = minFontPx

      while (low <= high) {
        const mid = Math.floor((low + high) / 2)
        container.style.fontSize = `${mid}px`

        const overflows = container.scrollWidth > container.clientWidth

        if (!overflows) {
          best = mid
          low = mid + 1
        } else {
          high = mid - 1
        }
      }

      // Set final font size via state
      setComputedFontSize(best)
    }

    const resizeObserver = new ResizeObserver(() => measureAndFit())
    resizeObserver.observe(container)

    // Initial measure after paint
    const raf = requestAnimationFrame(measureAndFit)

    return () => {
      cancelAnimationFrame(raf)
      resizeObserver.disconnect()
    }
  }, [text, minFontPx, maxFontPx])

  return (
    <div
      ref={containerRef}
      className={cn('w-full text-center leading-tight', className)}
      style={{ fontSize: `${computedFontSize}px` }}
      title={text}
    >
      {text}
    </div>
  )
}