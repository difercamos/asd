import DS from 'ember-data';

export default DS.Model.extend({
  nombre: DS.attr('string'),
  descripcion: DS.attr('string'),
  tipo: DS.attr('string'),
  serial: DS.attr('string'),
  numero_interno: DS.attr('string'),
  peso: DS.attr('string'),
  alto: DS.attr('string'),
  ancho: DS.attr('string'),
  largo: DS.attr('string'),
  valor_compra: DS.attr('string'),
  fecha_compra: DS.attr('string'),
  estado: DS.attr('string'),
  color: DS.attr('string'),
  ubicacion: DS.attr(),
  usuario: DS.attr('string')
});
