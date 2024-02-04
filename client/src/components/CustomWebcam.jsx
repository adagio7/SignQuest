import Webcam from "react-webcam";
import { useRef, useState, useCallback } from "react";
import "./CustomWebcam.css"; // Import a CSS file for styling

const CustomWebcam = () => {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);
  }, []);

  return (
    <div className="webcam-container">
      <Webcam
        audio={false}
        ref={webcamRef}
        height={600}
        width={600}
        screenshotFormat="image/jpeg"
        mirrored={true} // Set the mirrored prop to true
      />
      {/* <button onClick={capture}>Capture Photo</button>
      {imgSrc && <img src={imgSrc} alt="Captured" />} */}
    </div>
  );
};

export default CustomWebcam;
