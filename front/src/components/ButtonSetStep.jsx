import React, {useEffect, useState} from 'react';

function ButtonSetStep({set}) {
    // remember 0 - nothing 1 - X 2 - 0
    const button_size = 10;
    const [data_tic, set_data_tic] = useState(set);
    const [is_hovered, set_is_hovered] = useState(false);


    console.log(data_tic);

    return(
        <div className={"w-"+button_size+" h-"+button_size+""}>

            {
                data_tic === 0 &&
                <button
                    onMouseEnter={() => set_is_hovered(true)}
                    onMouseLeave={() => set_is_hovered(false)}
                    className={"bg-gray-300 w-"+button_size+" h-"+button_size+" border border-black "}>

                    {is_hovered && <p className="display-on-hover">X</p>}
                </button>
            }
            {
                data_tic === 1 &&
                <div className={"w-"+button_size+" h-"+button_size+" bg-gray-300 flex items-center border border-black justify-center "}>
                    <p>X</p>

                </div>
            }
            {
                data_tic === 2 &&
                <div className={"w-"+button_size+" h-"+button_size+" bg-gray-300 flex items-center border border-black justify-center "}>
                    <p>O</p>
                </div>
            }

        </div>
    );
}

export default ButtonSetStep;