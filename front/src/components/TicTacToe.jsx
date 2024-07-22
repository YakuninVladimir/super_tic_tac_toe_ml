import React from 'react';
import Cell from "./Cell";

function TicTacToe(props) {
    return (
        <div >
            <div className={"flex"}>
                <Cell/>
                <Cell/>
                <Cell/>
            </div>
            <div className={"flex"}>
                <Cell/>
                <Cell/>
                <Cell/>
            </div>
            <div className={"flex"}>
                <Cell/>
                <Cell/>
                <Cell/>
            </div>
        </div>
    );
}

export default TicTacToe;