"D:\RealityCapture\RealityCapture.exe" ^
-addFolder "%~dp0Testa2.0" ^
-setProjectCoordinateSystem Local:1 ^
-detectMarkers "%~dp0detectSettings.xml" ^
-importGroundControlPoints "%~dp0markerPositions.csv" "%~dp0gcpSettings.xml" ^
-align ^
-calculatePreviewModel ^
-selectLargeTrianglesRel 30 ^
-removeSelectedTriangles ^
-setReconstructionRegion "%~dp0object.rcbox" ^
-calculateNormalModel ^
-selectLargestModelComponent ^
-calculateTexture ^
-simplify "%~dp0simplifySettings.xml" ^
-save "%~dp0Testa2.0.rcproj" ^
-exportSelectedModel "%~dp0model\Testa2.0.obj" "%~dp0exportSettings.xml"
 