import { Metadata } from 'next';
import siteConfig from '@/lib/og/site.json';

export const metadata: Metadata = {
  title: siteConfig.title,
  openGraph: {
    title: siteConfig.title,
    images: [
      {
        url: '/og.jpg',
        width: 1200,
        height: 630,
        alt: siteConfig.title,
      },
   ],
  },
  icons: {
    icon: '/favicon.ico', 
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body style={{ margin: 0, background: '#020617', color: '#fff' }}>
        {children}
      </body>
    </html>
  );
}
