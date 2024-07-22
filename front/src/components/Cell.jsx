import React from 'react';
import ButtonSetStep from "./ButtonSetStep";

function Cell(props) {
    return (
        <div className={"grid grid-cols-3"}>
            {props.row.map((cell, cellIndex)=>(
                <ButtonSetStep key={cellIndex} function={props.function} rowIndex={props.row_index} cellIndex={cellIndex}  set={cell}/>

            ))}
        </div>
    );
}

export default Cell;