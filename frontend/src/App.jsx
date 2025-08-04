import React, { useEffect, useState } from 'react';

function Header(){
  return(<Header classname="header">
    <h1>FromPdfToAudio</h1>
    <p>Convert PDF files to audio files</p>
  </Header>)
}
function App() {
   const [currentView, setCurrentView] = useState('home');
   const [pdfText, setpdfText] = useState('');
   const [audioFile, setAudioFile] = useState(null);
   const [error, setError] = useState(''); 
   const [loading, setLoading] = useState(false);
   const[succes , setSucces]= useState(false);  
   useEffect
  
  
  
  
  
  
  }

function Footer() {
  return (
    <footer>
      <p>© 2025</p>
    </footer>
  );
}
