import Ember from 'ember';

export default Ember.Controller.extend({
  estado: "",
  actions: {
      selectEstado: function(estado){
        this.set('estado', estado);
      },
      createActivo: function(){
        var self = this;
        let newActivo = this.get('store').createRecord('activo', {
          nombre: self.get('nombre'),
          descripcion: self.get('descripcion'),
          tipo: self.get('tipo'),
          serial: self.get('serial'),
          numero_interno: self.get('numero_interno'),
          peso: self.get('peso'),
          alto: self.get('alto'),
          ancho: self.get('ancho'),
          largo: self.get('largo'),
          valor_compra: self.get('valor_compra'),
          fecha_compra: self.get('fecha_compra'),
          estado: self.get('estado'),
          color: self.get('color')
        });

      function transitionToIndex() {
        self.transitionToRoute('index');
      }

      function failure(reason) {
        alert(reason);
      }

      newActivo.save().then(transitionToIndex).catch(failure);
    }
  }
});
