import React from "react";

function Rating({ value, text, color }) {
    const stars = [];

    for (var index = 0; index < 5; index++) {
        stars.push(
            <i
                key={`${index}`}
                style={{ color }}
                className={
                    value >= index + 1
                        ? "fas fa-star"
                        : value >= index + 0.5
                        ? "fas fa-star-half-alt"
                        : "far fa-star"
                }
            />
        );
    }

    return (
        <div className="rating">
            <span>{stars}</span>
            <span>{text && text}</span>
        </div>
    );
}

export default Rating;
