import Webcam from "react-webcam";
import { useRef } from "react";

const CustomWebcam = () => {
    const webcamRef = useRef(null);

    return (
        <Webcam
            audio={false}
            ref={webcamRef}
            height={600}
            width={600}
            screenshotFormat="image/jpeg"
        />
    );
}

export default CustomWebcam;