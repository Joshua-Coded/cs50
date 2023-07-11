// import all the contaienrs
import { About, Header, Partnership, Footer, Project, Usecases } from "./container";
import { Navbar } from "./components";

import './App.scss';

function App() {
  return (
    <div className="app">
      <Navbar />
      <Header />
      <About />
      <Project />
      <Partnership />
      <Usecases />
      <Footer />
    </div>
  );
}

export default App;
