import { Inter as FontSans } from "next/font/google";

import { cn } from "@/lib/utils";

import "./globals.css";
import { Metadata } from "next";

const fontSans = FontSans({
  subsets: ["latin"],
  variable: "--font-sans",
});

export const metadata: Metadata = {
  title: "FF15",
  description: "Best LoL current game ",
  keywords:
    "FF15, LoL, LoL stats, League of Legends, league of legends players stats, league of legends user stats, league of legends game stats, stats for league of legends, statistics league of legends, league legends stats",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={cn("min-h-screen font-sans antialiased", fontSans.variable)}
      >
        {children}
      </body>
    </html>
  );
}
