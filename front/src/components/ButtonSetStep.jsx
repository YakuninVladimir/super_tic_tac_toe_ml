import React, {useEffect, useState} from 'react';
import {CELL_STATE} from "./TicTacToe";



function ButtonSetStep(props) {
    // remember 0 - nothing 1 - X 2 - 0
    const button_size = 10;


    return(
        <div className={"w-"+button_size+" h-"+button_size+""}>

            {
                props.set === CELL_STATE.EMPTY &&
                <button
                    onClick={()=>{props.function(props.rowIndex, props.cellIndex)}}
                    className={"bg-gray-300 w-"+button_size+" h-"+button_size+" border border-black "}>

                </button>
            }
            {
                props.set === CELL_STATE.X &&
                <div className={"w-"+button_size+" h-"+button_size+" bg-gray-300 flex items-center border border-black justify-center "}>
                    <p>X</p>

                </div>
            }
            {
                props.set === CELL_STATE.O &&
                <div className={"w-"+button_size+" h-"+button_size+" bg-gray-300 flex items-center border border-black justify-center "}>
                    <p>O</p>
                </div>
            }

        </div>
    );
}

export default ButtonSetStep;