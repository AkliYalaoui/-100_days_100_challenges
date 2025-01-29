const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-800 text-gray-400 py-6">
      <div className="container mx-auto text-center">
        <p className="text-sm mb-2">
          Maze Generator by{" "}
          <a
            href="https://github.com/akliyalaoui"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:text-blue-300 transition-colors"
          >
            Akli Yalaoui
          </a>
          , © {currentYear}
        </p>
        <p className="text-sm">
          Feel free to fork the{" "}
          <a
            href="https://github.com/AkliYalaoui/-100_days_100_challenges"
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:text-blue-300 transition-colors"
          >
            GitHub repo
          </a>
          .
        </p>
      </div>
    </footer>
  );
};

export default Footer;