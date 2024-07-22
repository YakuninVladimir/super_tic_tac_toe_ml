import React, {useState} from 'react';
import Cell from "./Cell";

 const CELL_STATE  = {
    X: 1,
    O: 2,
    EMPTY: 0
}


function TicTacToe(props) {
    const initialArray = Array.from({length: 9}, () =>
        Array.from({length: 9}, () => CELL_STATE.EMPTY)
    );

    const [grid, setGrid] = useState(initialArray);
    const [isPlayerX, setIsPlayerX] = useState(true);
    const handleButtonClick = (row, col) => {

        grid[row][col] = isPlayerX ? CELL_STATE.X : CELL_STATE.O;
        setIsPlayerX((prevState) => !prevState);

    };
    console.log(grid)
    return (
        <div className={"grid grid-cols-3"}>
            {grid.map((row, row_index) => (

                <Cell key={row_index} row={row} row_index={row_index} function={handleButtonClick}/>


            ))}
        </div>
    );
}

export {CELL_STATE};

export default TicTacToe;