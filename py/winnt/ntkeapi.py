from enum import IntEnum

KTHREAD_STATE = IntEnum('KTHREAD_STATE', (
   'Initialized',
   'Ready',
   'Running',
   'Standby',
   'Terminated',
   'Waiting',
   'Transition',
   'DefferedReady',
   'GateWaitObsolete',
   'WaitingForProcessInSwap',
   'MaximumThreadState'
), start=0)

KWAIT_REASON = IntEnum('KWAIT_REASON', (
    'Executive',
    'FreePage',
    'PageIn',
    'PoolAllocation',
    'DelayExecution',
    'Suspended',
    'UserRequest',
    'WrExecutive',
    'WrFreePage',
    'WrPageIn',
    'WrPoolAllocation',
    'WrDelayExecution',
    'WrSuspended',
    'WrUserRequest',
    'WrEventPair',
    'WrQueue',
    'WrLpcReceive',
    'WrLpcReply',
    'WrVirtualMemory',
    'WrPageOut',
    'WrRendezvous',
    'WrKeyedEvent',
    'WrTerminated',
    'WrProcessInSwap',
    'WrCpuRateControl',
    'WrCalloutStack',
    'WrKernel',
    'WrResource',
    'WrPushLock',
    'WrMutex',
    'WrQuantumEnd',
    'WrDispatchInt',
    'WrPreempted',
    'WrYieldExecution',
    'WrFastMutex',
    'WrGuardedMutex',
    'WrRundown',
    'WrAlertByThreadId',
    'WrDeferredPreempt',
    'MaximumWaitReason'
), start=0)