export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body>
        <nav style={{ padding: "10px", borderBottom: "1px solid #ccc" }}>
          <a href="/">Home</a> |{" "}
          <a href="/about">About</a> |{" "}
          <a href="/contact">Contact</a>
        </nav>

        {children}
      </body>
    </html>
  );
}