const Card = () => {
    return (
      <div className="w-full max-w-md bg-gray-500 shadow-xl rounded-2xl overflow-hidden">
        <img
          className="w-full h-60 object-cover"
          src="https://thvnext.bing.com/th/id/OIP.V8YqHho4NXzm5hLHdai7MQHaFj?w=233&h=180&c=7&r=0&o=7&cb=ucfimgc2&pid=1.7&rm=3"
          alt="Imagem Ilustrativa"
        />
        <div className="p-6 text-center">
          <h2 className="text-2xl font-bold text-gray-900">Doguinhos</h2>
          <p className="text-gray-600 mt-3">
            Rs
          </p>
          <button className="mt-5 w-full bg-red-800 text-white py-3 rounded-lg text-lg font-semibold hover:bg-blue-600 transition duration-300">
            Botão
          </button>
        </div>
      </div>
    );
  };
  
  export default Card;