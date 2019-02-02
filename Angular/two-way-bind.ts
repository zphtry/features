export class ChildComponent{
  @Input() amount;

/* Key  feature is «Change» suffix after variable name*/
  @Output() amountChange = new EventEmitter();
}
