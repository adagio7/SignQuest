import Webcam from "react-webcam";
import { 
    useRef,
    useState,
    useCallback 
} from "react";

const CustomWebcam = () => {
    const webcamRef = useRef(null);
    const [imgSrc, setImgSrc] = useState(null);

    const capture = useCallback(() => {
        const imageSrc = webcamRef.current.getScreenshot();
        setImgSrc(imageSrc);
    })

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