import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import Project from "./pages/Project";
import About from "./pages/About";
import "./styles/globals.css";

function App() {
  return (
    <>
      <BrowserRouter>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/project" element={<Project />} />
            <Route path="/About" element={<About />} />
          </Routes>
        </Layout>
      </BrowserRouter>
    </>
  );
}

export default App;
