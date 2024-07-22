import { Inter as FontSans } from "next/font/google"

import { cn } from "@/lib/utils"

import "./globals.css"
import { Metadata } from "next"

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
})

export const metadata: Metadata = {
  title: "FF15",
  description: "Best LoL current game ",
  keywords: "FF15, LoL, LoL stats, League of Legends, LoL champs, LoL current game, LoL active game, LoL live game, statistics, LoL spectate"
}

export default function RootLayout({ children }: {children: React.ReactNode}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={cn(
          "min-h-screen font-sans antialiased",
          fontSans.variable
        )}
      >
        {children}
      </body>
    </html>
  )
}
