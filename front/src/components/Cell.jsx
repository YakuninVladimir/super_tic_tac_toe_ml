import React from 'react';
import ButtonSetStep from "./ButtonSetStep";

function Cell(props) {
    return (
        <div>
            <div className={"flex"}>
                <ButtonSetStep set={1}/>
                <ButtonSetStep set={0}/>
                <ButtonSetStep set={2}/>

            </div>
            <div className={"flex"}>
                <ButtonSetStep set={0}/>
                <ButtonSetStep set={0}/>
                <ButtonSetStep set={0}/>

            </div>
            <div className={"flex"}>
                <ButtonSetStep set={1}/>
                <ButtonSetStep set={2}/>
                <ButtonSetStep set={1}/>

            </div>


        </div>
    );
}

export default Cell;