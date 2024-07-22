import './App.css';
import NavBar from "./components/NavBar";
import TicTacToe from "./components/TicTacToe";
import ButtonSetStep from "./components/ButtonSetStep";

function App() {
  return (
    <div className="App">
     <NavBar/>
        <div className={"pt-10 flex w-full justify-center items-center"}>
            <TicTacToe/>
        </div>
    </div>
  );
}

export default App;
